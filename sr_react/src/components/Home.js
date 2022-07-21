import React ,{useRef, useEffect,useState} from 'react';
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../App.css";
import {Map, MarkerClusterer,MapMarker} from 'react-kakao-maps-sdk'
import axios from "axios";

const {kakao} = window;

const Home = () => {

  const mapRef = useRef();
  const [building, buildingList] = useState([]);

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

  //여기서 누르면 리스트나오게ㅇㅇ
  const onClusterclick = (_target, cluster) => {
    // const map = mapRef.current
    // // 현재 지도 레벨에서 1레벨 확대한 레벨
    // const level = map.getLevel() - 1;

    // // 지도를 클릭된 클러스터의 마커의 위치를 기준으로 확대합니다
    // map.setLevel(level, {anchor: cluster.getCenter()});
    console.log(cluster);

  };

  return (
    <div className='map'>
      
    <Map // 지도를 표시할 Container
        center={{
          // 지도의 중심좌표
          lat: 35.83222044838787,
          lng: 128.75789218849744,
        }}
        style={{
          // 지도의 크기
          width: "100%",
          height: "450px",
        }}
        level={6} // 지도의 확대 레벨
        ref={mapRef}
      >
        <MarkerClusterer
          averageCenter={true} // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
          minLevel={5} // 클러스터 할 최소 지도 레벨
          disableClickZoom={true} // 클러스터 마커를 클릭했을 때 지도가 확대되지 않도록 설정한다
          // 마커 클러스터러에 클릭이벤트를 등록합니다
          // 마커 클러스터러를 생성할 때 disableClickZoom을 true로 설정하지 않은 경우
          // 이벤트 헨들러로 cluster 객체가 넘어오지 않을 수도 있습니다
          onClusterclick={onClusterclick}
        >
          {building.map((pos) => (
            <MapMarker
              key={`${pos.lat}-${pos.lng}`}
              position={{
                lat: pos.lat,
                lng: pos.lng,
              }}
            />
          ))}
        </MarkerClusterer>
      </Map>

    </div>
  );
};

export default Home;

