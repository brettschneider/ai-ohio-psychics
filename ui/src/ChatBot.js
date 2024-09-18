import "./ChatBot.css"
import { Button, Form, Modal, Spinner } from "react-bootstrap";
import { useStateDispatch } from "./ApplicationState"
import { Chat } from "react-bootstrap-icons"
import { useEffect, useRef, useState } from "react";

export const ChatBotButton = () => {
    const { state, dispatch } = useStateDispatch();
    const openChat = () => {
        dispatch({ type: "OPEN_CHAT" });
    };
    return state.token ? (
        <div>
            <Button
                variant="primary"
                onClick={openChat}
                style={{
                    position: 'fixed',
                    bottom: '20px',
                    right: '20px',
                    borderRadius: '50%',
                    padding: '10px 15px'
                }}>
                <Chat size={24} />
            </Button>
        </div>
    ) : null
}

export const ChatBotWindow = () => {
    const { state, dispatch } = useStateDispatch();
    const [userInput, setUserInput] = useState('');
    const [messages, setMessages] = useState([]);
    const [sendDisabled, setSendDisabled] = useState(false);
    const chatEndRef = useRef(null);

    const hideChat = () => {
        setMessages([]);
        setUserInput('');
        dispatch({ type: "CLOSE_CHAT" });
    }

    const addMessage = (message) => {
        setMessages(prevMessages => [...prevMessages, message]);
    };

    const updateLastBotMessage = (text) => {
        setMessages(prevMessages => {
            const updatedMessages = [...prevMessages];
            const lastMessageIndex = updatedMessages.length - 1;
            if (lastMessageIndex >= 0 && updatedMessages[lastMessageIndex].sender === 'bot') {
                updatedMessages[lastMessageIndex] = { ...updatedMessages[lastMessageIndex], text };
            } else {
                updatedMessages.push({ sender: 'bot', text });
            }
            return updatedMessages;
        });
    };

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setSendDisabled(true);
        if (userInput.trim()) {
            addMessage({ sender: 'user', text: userInput });
            try {
                const response = await fetch('http://localhost:8000/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json',
                        'x-token': state.token,
                    },
                    body: JSON.stringify({ query: userInput })
                });
                if (response.body) {
                    const reader = response.body.getReader();
                    let done, value, botMessage = '';
                    while (!done) {
                        ({ value, done } = await reader.read());
                        if (done) break;
                        botMessage += new TextDecoder().decode(value);
                        updateLastBotMessage(botMessage);
                    }
                    setSendDisabled(false);
                }
            } catch (error) {
                alert(`Problem chatting with server: ${error}`);
            }
            setUserInput('');
        }
    }

    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    return (
        <Modal show={state.chatOpen} onHide={hideChat} centered>
            <Modal.Header closeButton>Ohio Psyc Virtual Assistant</Modal.Header>
            <Modal.Body>
                <div style={{ minHeight: '300px', maxHeight: '300px', overflowY: 'auto', marginBottom: '10px' }}>
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.sender}`} dangerouslySetInnerHTML={{ __html: msg.text.replace("\n", "<br>") }}></div>
                    ))}
                    <div ref={chatEndRef} />
                </div>
                <Form onSubmit={handleSubmit} autoComplete="off">
                    <Form.Group controlId="chatInput">
                        <Form.Control
                            type="text"
                            placeholder="Type a message..."
                            value={userInput}
                            onChange={handleInputChange}
                            disabled={sendDisabled}
                        />
                    </Form.Group>
                    <Button variant="primary" type="submit" className="mt-2" disabled={sendDisabled || !userInput}>
                        Send
                    </Button>
                    &nbsp;
                    <Button className="mt-2" variant="outline-dark" hidden={!sendDisabled}>
                        <Spinner hidden={!sendDisabled} animation="grow" variant="primary" as="span" size="sm"></Spinner>
                    </Button>
                </Form>
            </Modal.Body>
        </Modal>
    )
}