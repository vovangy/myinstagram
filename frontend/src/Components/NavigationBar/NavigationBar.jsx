import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Navbar, Nav } from 'react-bootstrap';

const NavigationBar = () => {
    //const navigate = useNavigate();


    //const profileButtonHandler =  (event) => {
    //    navigate("/profile");
    //}

    return (<div>
        <Navbar bg="dark" expand="sm" variant="dark">
            <Container>
                <Navbar.Brand href='/profile'>Myinstagram</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-auto">
                        <Nav.Link href="/profile#profile">Профиль</Nav.Link>
                        <Nav.Link href="/feed#feed">Лента</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    </div>)
}

export default NavigationBar