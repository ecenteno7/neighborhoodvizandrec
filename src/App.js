import * as React from 'react';
import MapComponent from './components/MapComponent';
import atlanta_geojson from './resources/atlanta.geojson';
import chicago_geojson from './resources/chicago.geojson';

function App() {
  return (
    <div>
      <MapComponent 
        geojson={atlanta_geojson} 
        initialViewState={{
          longitude: -84.376656, 
          latitude: 33.749542, 
          zoom: 10}}>
      </MapComponent>
    </div>
  );
}

export default App;