import React from 'react';
import { useNavigate } from "react-router-dom";

const EachBd = ({ID, name, monthlyRent, avg}) => {
    const navigate = useNavigate();
    const goPost = () => {
        navigate(`${"/list/" + ID}`);
      };
    return (
        <div onClick={goPost}>
            <span>건물명 : {name}</span>
            <span>월세 : {monthlyRent}</span>
            <span>전체평점  {avg}</span>
            {/* <span>필터적용 : {e.id}</span> */}
        </div>
    );
};

export default EachBd;