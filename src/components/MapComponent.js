import React, { Component } from "react";
import Map, { Source, Layer } from "react-map-gl";

class MapComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      res: {
        neighborhoods: [
          {
            key: "West Midtown",
            description:
              "West Midtown, also known as Westside,[1] is a colloquial area, comprising many historical neighborhoods located in Atlanta, Georgia. Once largely industrial, West Midtown is now the location of urban lofts, art galleries, live music venues, retail and restaurants.",
            pointsOfInterest: [
              "Ormsby's",
              "Puttshack",
              "Fire Maker Brewing Company",
            ],
          },
          {
            key: "East Atlanta",
            description:
              "East Atlanta is a neighborhood on the east side of Atlanta, Georgia, United States. The name East Atlanta Village primarily refers to the neighborhood's commercial district.",
            pointsOfInterest: ["Ramen Place", "Coffee Shop", "Brewery"],
          },
          {
            key: "Candler Park",
            description:
              "Leafy Candler Park is a quiet, largely residential neighborhood, with late-19th- and early-20th-century homes. Community events are often held at landscaped Candler Park, which has a golf course, playground and swimming pool. Trails wind past outdoor art installations in adjacent Freedom Park. McLendon Avenue is home to laid-back cafes and restaurants that serve Southern food.",
            pointsOfInterest: ["Coffee", "Bar", "Movie Theater"],
          },
        ],
      },
    };
    let selectedNeighborhoods = [];
  }

  componentDidMount(prevProps) {
    const prefNeighborhoods = this.state.res.neighborhoods.map((interest) => {
      return interest.name;
    });
    this.props.geojson.features.map((feature) => {
      if (prefNeighborhoods.includes(feature.properties.name)) {
        this.state.selectedNeighborhoods.push(feature);
      }
    });
    console.log(this.state.selectedNeighborhoods);
  }

  layerStyle = {
    id: "point",
    type: "fill",
    paint: {
      "fill-color": "red",
      "fill-opacity": 0.2,
    },
  };

  render() {
    return (
      <Map
        mapboxAccessToken={process.env.REACT_APP_API_KEY}
        initialViewState={this.props.initialViewState}
        style={{ width: 600, height: 400, margin: "auto", padding: 20 }}
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
