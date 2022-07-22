import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { replace } = useNavigate();

  const onChangeUsername = (e) => {
    setUsername(e.target.value);
  };

  const onChangeEmail = (e) => {
    setEmail(e.target.value);
  };

  const onChangePassword = (e) => {
    setPassword(e.target.value);
  };

  const checkUser = () => {
    if (username === "" || email === "" || password === "") {
      alert("이름, 이메일, 비밀번호를 입력해주세요");
      return;
    }
    axios
      .post("http://127.0.0.1:8000/accounts/login/", {
        username: username,
        email: email,
        password: password,
      })
      .then(() => {
        alert("로그인 성공");
        console.log("Well done");
        //console.log("User token", response.data.jwt);
        //localStorage.setItem("token", response.data.jwt);
        replace("/"); //페이지 이동 함수
      })
      .catch((error) => {
        alert("로그인 실패");
        console.log("An error occured:", error.response);
      });
  };

  useEffect(() => {
    if (localStorage.getItem("token")) {
      replace("/"); //로그인 페이지안에서 render,다시 로그인으로 돌아올 일 없게 함
    }
  }, []);

  return (
    <form>
      <h3>Sign In</h3>
      <div className="mb-3">
        <label>UserName</label>
        <input
          type="string"
          className="form-control"
          placeholder="UserName"
          required
          //readOnly="false"
          label="Username"
          value={username}
          onChange={onChangeUsername}
        />
      </div>

      <div className="mb-3">
        <label>Email address</label>
        <input
          type="email"
          className="form-control"
          placeholder="Enter email"
          required
          //readOnly="false"
          label="Email"
          value={email}
          onChange={onChangeEmail}
        />
      </div>

      <div className="mb-3">
        <label>Password</label>
        <input
          type="string"
          className="form-control"
          placeholder="Enter password"
          required
          //readOnly="false"
          label="Password"
          value={password}
          onChange={onChangePassword}
        />
      </div>

      <div className="mb-3">
        <div className="custom-control custom-checkbox">
          <input
            type="checkbox"
            className="custom-control-input"
            id="customCheck1"
          />
          <label className="custom-control-label" htmlFor="customCheck1">
            Remember me
          </label>
        </div>
      </div>

      <div className="d-grid">
        <button type="submit" className="btn btn-primary" onClick={checkUser}>
          Submit
        </button>
      </div>
      <p className="forgot-password text-right">
        Forgot <a href="#">password?</a>
      </p>
    </form>
  );
};

export default Login;
