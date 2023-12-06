import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Navbar, Nav } from 'react-bootstrap';

const NavigationBar = () => {
    //const navigate = useNavigate();


    //const profileButtonHandler =  (event) => {
    //    navigate("/profile");
    //}

    const navigate = useNavigate();

    const logoutButtonHandler = (event) => {
        localStorage.removeItem('user_id');
        localStorage.removeItem('username');
        localStorage.removeItem('token');
        navigate("/")
    }

    const profileHandler = () => {
        localStorage.setItem("profile_id", localStorage.getItem("user_id"));
    }

    return (<div>
        <Navbar bg="dark" expand="sm" variant="dark">
            <Container>
                <Navbar.Brand href='/profile'>Myinstagram</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-auto">
                        <Nav.Link href="/profile/" onClick={profileHandler}>Профиль</Nav.Link>
                        <Nav.Link href="/feed#feed">Лента</Nav.Link>
                        <Nav.Link onClick={logoutButtonHandler}>Выйти</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    </div>)
}

export default NavigationBar