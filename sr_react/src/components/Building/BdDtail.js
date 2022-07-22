import React from 'react';
import "../../App.css";

const BdDtail = () => {
    return (
        <div className='component-wrapper'>
            <div className='map_left'>
                <div className='map_left_top'></div>
                <div className='map_left_bottom'></div>
            </div>
                <div className='map_right'>
                    <h1>월세 500/42</h1>
                    <p>경상북도 경산시 대학로 59길 25</p>
                        <div className="rating">
                            <p>청결순</p>
                            <div className="star"></div>
                        </div>    
                        <div className="rating">
                            <p>종합평점</p>
                            <div className="star"></div>
                            <div className="star"></div>
                            <div className="star"></div>

                        </div>
                    <div className="house"></div>
                    <div className='fav'>
                    환기가 정말 잘 돼요.
수압이 너무 약해요.
주인 아주머니가 정말 꼼꼼히 관리해주시고, 조용하게 살기 좋아요.
여름에 덥고, 겨울에 추워요...
방도 넓고 창문개수, 집 바로 앞에 편의점있어서 다 좋은데 술집근처라 저녁되면 술취한 사람들 때문에 많이 시끄러움

                    </div>
                    <button className='filterBtn'>
                    리뷰 등록하기
                    </button>
                </div>
     
        </div>
    );
};

export default BdDtail;