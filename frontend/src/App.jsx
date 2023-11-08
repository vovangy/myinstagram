import './App.css';
import { Routes ,Route, BrowserRouter} from 'react-router-dom';
import Login from './Pages/Login/Login';
import Feed from './Pages/Feed/Feed';
import Profile from './Pages/Profile/Profile';
import Registration from './Pages/Registration/Registration'
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element={ <Login/> }></Route>
      <Route path="/registration" element={ <Registration/> }></Route>
      <Route path="/feed" element={ <Feed/> }></Route>
      <Route path="/profile" element={ <Profile/> }></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
