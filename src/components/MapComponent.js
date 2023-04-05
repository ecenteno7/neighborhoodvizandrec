import React, { Component } from 'react';
import Map, {Source, Layer} from 'react-map-gl';

class MapComponent extends Component {
    constructor(props){
        super(props);
    }

    layerStyle = {
        id: 'point',
        type: 'fill',
        paint: {
          "fill-color": "red",
          "fill-opacity": 0.2
        }
    };

    render() {
        return (
            <Map
                mapboxAccessToken={process.env.REACT_APP_API_KEY}
                initialViewState = {this.props.initialViewState}
                style={{width: 600, height: 400, margin: 'auto'}}
                mapStyle="mapbox://styles/mapbox/streets-v9"
            >
                <Source id="my-data" type="geojson" data={this.props.geojson}>
                    <Layer {...this.layerStyle} />
                </Source>
            </Map>
        );
    }
}

export default MapComponent;
