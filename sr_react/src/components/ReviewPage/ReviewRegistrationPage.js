import React, { Component } from "react";
import "./StarRating.css";
import StarRating from "./StarRating";
import CheckBox from "./CheckBox";

class AddReview extends Component {
  constructor() {
    super();
    this.myRef = React.createRef();
    this.state = {
      reviewText: 0,
      reviewImgUrl: null,
      reviewData: 0,
      ratingValue: "",
      mapValue: [1, 2, 3, 4, 5],
    };
  }

  handleReviewText = (e) => {
    this.setState({
      reviewText: e.target.value,
    });
  };

  handleReviewImg = (e) => {
    this.setState({
      reviewImgUrl: e.target.value,
    });
  };

  render() {
    const { ratingValue, reviewText, mapValue } = this.state;
    const { reviewData, ratio } = this.props;
    const isValid = 50 <= reviewText.length;

    return (
      <div className="addReview">
        <h2>원룸 리뷰</h2>
        {/* <ReviewBoard reviewData={reviewData} ratio={ratio} /> */}
        <div className="rating"></div>
        <article className="addReviewArticle">
          <div className="input-group mb-3">
            <span className="input-group-text">월세</span>
            <input
              type="text"
              //class="form-control"
              aria-label="Amount (to the nearest dollar)"
              size={10}
            ></input>
            <span className="input-group-text">만원</span>
          </div>
          <div className="input-group mb-3">
            <span className="input-group-text">보증금</span>
            <input
              type="text"
              //class="form-control"
              aria-label="Amount (to the nearest dollar)"
              size={8}
            ></input>
            <span className="input-group-text">만원</span>
          </div>
          <form>
            <div>
              곰팡이
              <div>
                <StarRating id={1} />
              </div>
            </div>
            <br />
            <br />

            <div>
              벌레
              <StarRating id={2} />
            </div>
            <br />
            <br />
            <div>
              냄새
              <StarRating id={3} />
            </div>
            <br />
            <br />
            <div>
              내외소음
              <StarRating id={4} />
            </div>
            <br />
            <br />
            <div>
              외부소음
              <StarRating id={5} />
            </div>
            <br />
            <br />
            <div>
              층간소음
              <StarRating id={6} />
            </div>
            <br />
            <br />
            <div>
              주차공간
              <StarRating id={7} />
            </div>
            <br />
            <br />
            <div>
              관리
              <StarRating id={8} />
            </div>
            <br />
            <br />
            <div>
              구축/신축
              <StarRating id={9} />
            </div>
          </form>

          <CheckBox />
          <div className="reviewContent">
            <br />
            <br />
            <textarea
              cols="100"
              rows={5}
              placeholder="최소 50자 이상 입력해주세요"
              onChange={this.handleReviewText}
            ></textarea>
            <p>{reviewText ? reviewText.length : 0}/ 5,000</p>
          </div>
          <div>
            <div className="addImgBtn">
              <input
                type="file"
                accept="image/*"
                capture="user"
                onChange={this.handleReviewImg}
              />
            </div>
          </div>
        </article>
        <div className="btn">
          <button
            disabled={isValid ? false : true}
            className={isValid ? "activeBtn" : ""}
            onClick={this.uploadReviewData}
          >
            등록
          </button>
        </div>
      </div>
    );
  }
}

export default AddReview;
