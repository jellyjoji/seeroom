import React,{useState,useEffect} from 'react';
import { BrowserRouter as Routes, Route, Link, useNavigate } from "react-router-dom";
import "../../App.css";
import axios from "axios";
import BdDtail from './BdDtail';

const BuildList = () => {
    const [building, buildingList] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {

        axios
        .get("http://127.0.0.1:8000/reviews/building/")
        .then((response)=>{
          buildingList([...response.data]);
          console.log(response.data);
        })
        .catch(function(error){
            console.log(error);
        })    
      },[])
      const onClickBd = (id) => {
        
        navigate(`/list/${id}`);
      };
    
    return (
        <div className='component-wrapper'>
            <div className="list" >
            {building.map((e)=>(
                // <Link className="nav-link" to={`/building/${e.id}`}>
                <div onClick={onClickBd(e.id)}>

                    <span>
                        건물명 : {e.name} 
                    </span>
                    <span>
                        월세 : {e.monthlyRent} 
                    </span>
                    <span>
                        전체평점  {(e.cleanAvg+e.noiseAvg+e.locationsAvg+e.safeAvg)/4} 
                    </span>
                    {/* <span>
                        필터적용 : {e.id} 
                    </span> */}
                </div>
                // </Link>
            ))}
        </div>
            {/* <Routes>
                <Route path="/list" element={<BdDtail />} />
            </Routes> */}
        </div>

    );
};

export default BuildList;