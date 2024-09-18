import './App.css';
import { StateProvider } from './ApplicationState';
import { Col, Container, Row } from 'react-bootstrap';
import { Header } from './Header';
import { Route, Routes } from 'react-router-dom';
import { Login } from './Login';
import { Home } from './Home';
import { ChatBotButton, ChatBotWindow } from './ChatBot';

const App = () => (
  <StateProvider>
    <Header></Header>
    <Container>
      <Row>
        <Col>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </Col>
      </Row>
      <Row>
      </Row>
    </Container>
    <ChatBotButton />
    <ChatBotWindow />
  </StateProvider>
);

export default App;