import React from 'react';
import "../../App.css";

const BdDtail = () => {
    const Params = useParams();
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/reviews/building/${Params.BdID}`).then((response) => {
          console.log(response);
          setPost(response.data);
          setPostLoading(false);
          setRepls(response.data.repls);
          setReplLoading(false);
          replInput.current.focus();
        });
      }, []);
    
    return (
        <div className='component-wrapper'>
            디테이린아러ㅣㄴ어래ㅣㄷ
     
        </div>
    );
};

export default BdDtail;