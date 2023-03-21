import React, {useState} from 'react'


export default function Map() {

    const [count, setCount] = useState(0);

    const handleClick = (e) => {
        setCount(count + 1);
    }

    return (
        <>
            <button onClick={handleClick}></button>
            <div>Map</div>
            <p>{count}</p>
        </>
    )
}
