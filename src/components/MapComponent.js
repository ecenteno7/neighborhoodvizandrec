import React, {useState} from 'react'
import Map from 'react-map-gl';


export default function MapComponent() {

    const [count, setCount] = useState(0);

    const handleClick = (e) => {
        setCount(count + 1);
    }

    return (
        <>
            <button onClick={handleClick}></button>
            <div>Map</div>
            <p>{count}</p>
            <Map
                mapboxAccessToken={process.env.REACT_APP_API_KEY}
                initialViewState={{
                    longitude: -84.386330,
                    latitude: 33.73,
                    zoom: 12
                }}
                style={{width: 600, height: 400}}
                mapStyle="mapbox://styles/mapbox/streets-v9"
            />
        </>
    )
}
