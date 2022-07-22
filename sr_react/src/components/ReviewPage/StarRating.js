import React from "react";
import "./StarRating.css";

const StarRating = ({ id }) => {
  return (
    <form>
      <fieldset className="rating">
        <input type="radio" id={`star5${id}`} name="rating" value="5" />
        <label
          className="full"
          for={`star5${id}`}
          title="Awesome - 5 stars"
        ></label>

        <input type="radio" id={`star4half${id}`} name="rating" value="4.5" />
        <label
          className="half"
          for={`star4half${id}`}
          title="Pretty good - 4.5 stars"
        ></label>

        <input type="radio" id={`star4${id}`} name="rating" value="4" />
        <label
          className="full"
          for={`star4${id}`}
          title="Pretty good - 4 stars"
        ></label>

        <input type="radio" id={`star3half${id}`} name="rating" value="3.5" />
        <label
          className="half"
          for={`star3half${id}`}
          title="Meh - 3.5 stars"
        ></label>

        <input type="radio" id={`star3${id}`} name="rating" value="3" />
        <label
          className="full"
          for={`star3${id}`}
          title="Meh - 3 stars"
        ></label>

        <input type="radio" id={`star2half${id}`} name="rating" value="2.5" />
        <label
          className="half"
          for={`star2half${id}`}
          title="Kinda bad - 2.5 stars"
        ></label>
        <input type="radio" id={`star2${id}`} name="rating" value="2" />
        <label
          className="full"
          for={`star2${id}`}
          title="Kinda bad - 2 stars"
        ></label>
        <input type="radio" id={`star1half${id}`} name="rating" value="1.5" />
        <label
          className="half"
          for={`star1half${id}`}
          title="Meh - 1.5 stars"
        ></label>
        <input type="radio" id={`star1${id}`} name="rating" value="1" />
        <label
          className="full"
          for={`star1${id}`}
          title="Sucks big time - 1 star"
        ></label>
        <input type="radio" id={`starhalf${id}`} name="rating" value="0.5" />
        <label
          className="half"
          for={`starhalf${id}`}
          title="Sucks big time - 0.5 stars"
        ></label>
      </fieldset>
    </form>
  );
};

export default StarRating;
