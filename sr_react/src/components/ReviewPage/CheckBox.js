import React from "react";
import "./CheckBox.css";

const CheckBox = () => {
  return (
    <div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

      <div className="check-menu-box">
        <div className="checkbox-container">
          <input type="checkbox" id="checkbox2" name="checkOne" />
          <label for="checkbox2">엘리베이터</label>
        </div>
        <div className="checkbox-container">
          <input type="checkbox" id="checkbox3" name="checkOne" />
          <label for="checkbox3">여성전용</label>
        </div>
        <div className="checkbox-container">
          <input type="checkbox" id="checkbox4" name="checkOne" />
          <label for="checkbox4">CCTV</label>
        </div>
        <div className="checkbox-container">
          <input type="checkbox" id="checkbox5" name="checkOne" />
          <label for="checkbox5">무인택배함</label>
        </div>
      </div>
    </div>
  );
};

export default CheckBox;
