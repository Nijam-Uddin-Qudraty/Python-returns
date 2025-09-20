import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import ProtectedRoute from "./components/ProtectedRoute"
import Home from "./pages/Home"
import Login from "./pages/Login"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound"


function Logout() {
  localStorage.clear
  return <Navigate to="/login"/>
}

function RegAndLogout(){
  localStorage.clear
  return <Register />
}



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ProtectedRoute>
            <Home />
          </ProtectedRoute>}>
            </Route>
        
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<RegAndLogout />} />
          <Route path="*" element={<NotFound />}/>
        </Routes>
        
      </BrowserRouter>
    </>
  )
}

export default App
