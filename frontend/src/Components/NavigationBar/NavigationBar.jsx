import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Navbar, Nav } from 'react-bootstrap';
import axios from 'axios';

const NavigationBar = () => {
    //const navigate = useNavigate();


    //const profileButtonHandler =  (event) => {
    //    navigate("/profile");
    //}

    const navigate = useNavigate();

    const logoutButtonHandler = async (event) => {
        localStorage.removeItem('user_id');
        localStorage.removeItem('username');
        const headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token').replace("\"", "").replace("\"", ""),
        };
        console.log(headers);
        const response = await axios.post("http://127.0.0.1:8000/api/auth/token/logout", [], {headers: headers});
        localStorage.removeItem('token');
        navigate("/")
    }

    const profileHandler = () => {
        localStorage.setItem("profile_id", localStorage.getItem("user_id"));
    }

    return (<div>
        <Navbar bg="dark" expand="sm" variant="dark">
            <Container>
                <Navbar.Brand href='/feed'>Myinstagram</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-auto">
                        <Nav.Link href={"/profile/" + localStorage.getItem("user_id")}  onClick={profileHandler}>Профиль</Nav.Link>
                        <Nav.Link href="/feed">Лента</Nav.Link>
                        <Nav.Link href="/search">Поиск</Nav.Link>
                        <Nav.Link onClick={logoutButtonHandler}>Выйти</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    </div>)
}

export default NavigationBar