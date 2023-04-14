import React, { Component, useMemo} from "react";
import InteractiveMap, { Source, Layer } from "react-map-gl";

class MapComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      initGeoJson: this.props.geojson.features,
      selectedNeighborhoods: [],
      selectedNeighborhoodsGeoJson: {},
      res: {
        neighborhoods: this.props.res == null ? [] : this.props.res.neighborhoods,
        // neighborhoods: [
        //   {
        //     key: "West Midtown",
        //     description:
        //       "West Midtown, also known as Westside,[1] is a colloquial area, comprising many historical neighborhoods located in Atlanta, Georgia. Once largely industrial, West Midtown is now the location of urban lofts, art galleries, live music venues, retail and restaurants.",
        //     pointsOfInterest: [
        //       "Ormsby's",
        //       "Puttshack",
        //       "Fire Maker Brewing Company",
        //     ],
        //   },
        //   {
        //     key: "East Atlanta",
        //     description:
        //       "East Atlanta is a neighborhood on the east side of Atlanta, Georgia, United States. The name East Atlanta Village primarily refers to the neighborhood's commercial district.",
        //     pointsOfInterest: ["Ramen Place", "Coffee Shop", "Brewery"],
        //   },
        //   {
        //     key: "Candler Park",
        //     description:
        //       "Leafy Candler Park is a quiet, largely residential neighborhood, with late-19th- and early-20th-century homes. Community events are often held at landscaped Candler Park, which has a golf course, playground and swimming pool. Trails wind past outdoor art installations in adjacent Freedom Park. McLendon Avenue is home to laid-back cafes and restaurants that serve Southern food.",
        //     pointsOfInterest: ["Coffee", "Bar", "Movie Theater"],
        //   },
        // ],
      },
    };
  }

  componentDidMount(prevProps) {
    const prefNeighborhoods = this.state.res.neighborhoods.map((interest) => {
      return interest.key;
    });

    console.log(prefNeighborhoods);

    if (this.state.selectedNeighborhoods.length == 3) {
      return;
    }

    this.props.geojson.features.map((feature) => {
      if (prefNeighborhoods.includes(feature.properties.name)) {
        this.setState({
          selectedNeighborhoods: this.state.selectedNeighborhoods.push(feature),
        });
      }
    });

    this.setState({
      renderInitGeoJson: {
        type: "FeatureCollection",
        features: this.state.initGeoJson,
      },
    });
    this.setState({
      selectedNeighborhoodsGeoJson: {
        type: "FeatureCollection",
        features: this.state.selectedNeighborhoods,
      },
    });
    console.log(this.state.selectedNeighborhoodsGeoJson);
  }

  layerStyle = {
    id: "neighborhoods",
    type: "fill",
    paint: {
      "fill-color": "red",
      "fill-opacity": 0.2,
    },
  };

  hoverLayerStyle = {
    id: "hover",
    type: "fill",
    paint: {
      "fill-color": "green",
      "fill-opacity": 0.6,
    },
  };

  selectedLayerStyle = {
    id: "selected",
    type: "fill",
    paint: {
      "fill-color": "blue",
      "fill-opacity": 0.6,
    },
  };

  _onClick = event => {
    const {
      features,
      // srcEvent: { offsetX, offsetY }
    } = event;
    // console.log(features[0].properties.name);
    this.props.clickedNeighborhood(features[0].properties.name);
  };

  render() {
    return (
      <InteractiveMap
        mapboxAccessToken={process.env.REACT_APP_API_KEY}
        initialViewState={this.props.initialViewState}
        style={{ width: 600, height: 400, margin: "auto", padding: 20 }}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        interactiveLayerIds={["neighborhoods"]}
        onClick={this._onClick}
      >
        <Source id="my-data" type="geojson" data={this.state.renderInitGeoJson}>
          <Layer key={"rest"} {...this.layerStyle} />
          <layer key={"hover"} {...this.hoverLayerStyle} filter={this.hoveredNeighborhood}/>
        </Source>
        <Source id="my-data-selected" type="geojson" data={this.state.selectedNeighborhoodsGeoJson}>
          <Layer key={"selected"} {...this.selectedLayerStyle} />
        </Source>
      </InteractiveMap>
    );
  }
}

export default MapComponent;
