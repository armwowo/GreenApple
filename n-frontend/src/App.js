import Navbar from "./Navbar"
import Home from "./Home"
import Login from "./Login"
import Register from "./Register"
import UserProfile from "./components/Profile"
import Sabaiplace from "./Sabaiplace"
import Reserve from "./Reserve"
import APPLEHOUSE from "./APPLEHOUSE"
import AdCha from "./Adchariya"
import Bankum from "./Bankum"
import BBCourt from "./BBCourt"
import APHouse from "./APHouse"
import Buri from "./BuriIris"
import Allsmile from "./Allsmile"
import Rimnam from "./Rimnam"
import Nop from "./Noppakaow"
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Navbar />
      <div>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/Login" element={<Login/>} />
          <Route path="/Register" element={<Register/>} />
          <Route path="/Profile" element={<UserProfile />} />
          <Route path="/Sabaiplace" element={<Sabaiplace/>} />
          <Route path="/APPLEHOUSE" element={<APPLEHOUSE/>} />
          <Route path="/Adchariya" element={<AdCha/>} />
          <Route path="/Bankhumkaow48" element={<Bankum/>} />
          <Route path="/BBCourt" element={<BBCourt/>} />
          <Route path="/APHouse" element={<APHouse/>} />
          <Route path="/BuriIris" element={<Buri/>} />
          <Route path="/Allsmile" element={<Allsmile/>} />
          <Route path="/Rimnam" element={<Rimnam/>} />
          <Route path="/Noppakaow" element={<Nop/>} />
          <Route path="/Reserve" element={<Reserve/>} />
        </Routes>
      </div>
    </>
  )
}

export default App