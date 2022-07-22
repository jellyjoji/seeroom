import React,{useState,useEffect} from 'react';
import { BrowserRouter as Routes, Route, Link, useNavigate } from "react-router-dom";
import "../../App.css";
import axios from "axios";
import BdDtail from './BdDtail';
import EachBd from "./EachBd";
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
                <EachBd
                    ID={e.id}
                    name={e.name}
                    monthlyRent={e.monthlyRent}
                    avg={(e.cleanAvg+e.noiseAvg+e.locationsAvg+e.safeAvg)/4}
                />
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