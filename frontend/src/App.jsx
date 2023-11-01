import './App.css';
import { Routes ,Route, BrowserRouter} from 'react-router-dom';
import Login from './Login';
import Moment from './Moment';


function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element={ <Login/> }></Route>
      <Route path="/moment" element={ <Moment/> }></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
