import React from 'react';
import { useNavigate } from "react-router-dom";

const EachBd = ({ID, name, monthlyRent, avg}) => {
    const navigate = useNavigate();
    const goPost = () => {
        navigate(`${"/list/" + ID}`);
      };
    return (
        <div>
            <div className='listCards' onClick={goPost}>
                <span className='cardTitle'>건물명 : {name}</span>
                <span>월세 : {monthlyRent}</span>
                <span>전체평점  {avg}</span>
                {/* <span className="filter">필터적용 : {e.id}</span> */}
            </div>
            {/* <div className="filter"></div> */}
        </div>
        
    );
};

export default EachBd;