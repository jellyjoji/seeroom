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

            <div className='filter'>
                <strong className='contentTitle'>필터</strong>
                <nav className='filter_content'>
                    <h3 className='filterTitle'>청결</h3>
                    <ul className='filter_ul'>
                        <li className='filter_li'>곰팡이</li>
                        <li className='filter_li'>벌레</li>
                        <li className='filter_li'>냄새</li>
                    </ul>
                </nav>
                <nav clssName='filter_content'>
                    <h3 className='filterTitle'>청결</h3>
                    <ul className='filter_ul'>
                        <li className='filter_li'>곰팡이</li>
                        <li className='filter_li'>벌레</li>
                        <li className='filter_li'>냄새</li>
                    </ul>
                </nav>                
                <nav clssName='filter_content'>
                    <h3 className='filterTitle'>청결</h3>
                    <ul className='filter_ul'>
                        <li className='filter_li'>곰팡이</li>
                        <li className='filter_li'>벌레</li>
                        <li className='filter_li'>냄새</li>
                    </ul>
                </nav>
                <button className='filterBtn'>
                    적용하기
                </button>
            </div>
        
            {/* <Routes>
                <Route path="/list" element={<BdDtail />} />
            </Routes> */}
        </div>

    );
};

export default BuildList;