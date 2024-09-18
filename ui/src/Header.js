import "./Header.css"
import { Button, Col, Container, Row } from "react-bootstrap"
import { useStateDispatch } from "./ApplicationState"
import { Link } from "react-router-dom";

export const LoginButton = () => (
    <Link to="/login">
        <Button variant="dark">Login</Button>
    </Link>
);

export const LogoutButton = (dispatch) => {

    const logout = () => {
        dispatch({type: "LOGOUT"})
        alert("You are now logged out.");
    }

    return (
        <Button variant="dark" onClick={logout}>Logout</Button>
    )
};

export const Header = () => {
    const { state, dispatch } = useStateDispatch();

    return (
        <div className="header">
            <Container>
                <Row>
                    <Col>
                        <h3>Welcome to Ohio Psychics!</h3>
                    </Col>
                    <Col className="d-flex align-items-center" style={{ display: "flex", justifyContent: "end" }}>
                        <span className="me-2">{state.userName ? state.userName : ''}</span>
                        {state.token ? LogoutButton(dispatch) : LoginButton()}
                    </Col>
                </Row>
            </Container>
        </div>
    )
}