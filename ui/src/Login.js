import { useState } from "react";
import "./Login.css";
import { login } from "./service";
import { Button, Form, FormGroup } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import { useStateDispatch } from "./ApplicationState";

export const Login = () => {
    const { dispatch } = useStateDispatch();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const nav = useNavigate();

    const attemptLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await login(username, password);
            console.log(response);
            dispatch({ type: "LOGIN", token: response.token, userName: response.username })
            setTimeout(() => { nav("/"); }, 0);
        } catch {
            alert("Login failed")
        }
    }

    return (
        <div>
            <h1>Login</h1>
            <Form className="login" onSubmit={attemptLogin} autoComplete="off">
                <FormGroup>
                    <Form.Label>Username</Form.Label>
                    <Form.Control value={username} onChange={(event) => setUsername(event?.target.value)} name="username"></Form.Control>
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" value={password} onChange={(event) => setPassword(event?.target.value)} name="password"></Form.Control>
                </FormGroup>
                <br />
                <Button type="submit">Login</Button>
                &nbsp;
                <Link to="/">
                    <Button>Cancel</Button>
                </Link>
            </Form>
        </div>
    )
}
