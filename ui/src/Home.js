import { Col, Row, Image } from "react-bootstrap";
import { useStateDispatch } from "./ApplicationState";


export const AuthenticatedHome = () => {
    const { state } = useStateDispatch();
    return (
        <div>
            <img src="/OhioPsychics.png" alt="Logo Image" width="100%" />
            <br />
            <br />
            <p>Welcome {state.userName}!  We just knew you'd come back!</p>
            <br />
            <h2>
                Explore by Mediums
            </h2>
            <p>
                Connect with one of our specialized advisors to get the clarity and the guidance you need.
            </p>
            <br />
            <Row>
                <Col md={4}>
                    <Image src="/medium_1.png" width={200} rounded>
                    </Image>
                    <h4>
                        Aurora Starweaver
                    </h4>
                </Col>
                <Col md={4}>
                    <Image src="/medium_2.png" width={200} rounded>
                    </Image>
                    <h4>
                        Rowan Psychiccianni
                    </h4>
                </Col>
                <Col md={4}>
                    <Image src="/medium_3.png" width={200} rounded>
                    </Image>
                    <h4>
                        Luna Nightshade
                    </h4>
                </Col>
                <Col md={4}>
                    <Image src="/medium_4.png" width={200} rounded>
                    </Image>
                    <h4>
                        Cassius Sightmore
                    </h4>
                </Col>
                <Col md={4}>
                    <Image src="/medium_5.png" width={200} rounded>
                    </Image>
                    <h4>
                        Diana Clairvoyance
                    </h4>
                </Col>
                <Col md={4}>
                    <Image src="/medium_6.png" width={200} rounded>
                    </Image>
                    <h4>
                    Emrys Foresight
                    </h4>
                </Col>
            </Row>
        </div>
    )
}


export const UnauthenticatedHome = () => {
    const { state } = useStateDispatch();
    return (
        <div>
            <img src="/OhioPsychics.png" alt="Logo Image" width="100%" />

            <h3>Your Trusted Source for Insight and Guidance!</h3>

            <p>
                At Ohio Psychics, we understand that life can be full of uncertainties. Whether you're seeking clarity on love, career, finances, or personal growth, our gifted psychics are here to provide you with the answers and guidance you need. With just one call, our experienced advisors can help you navigate life’s challenges and uncover the path to your true potential.
            </p>

            <h3>Why Choose Ohio Psychics?</h3>

            <ul>
                <li><b>Experienced and Gifted Advisors:</b> Our team is made up of carefully selected psychics who possess a deep understanding of the spiritual realm. With years of experience, they offer reliable and accurate readings that can illuminate your path forward.</li>
                <li><b>Confidential and Caring Service:</b> We value your privacy and understand the sensitive nature of psychic readings. Every consultation is conducted with the utmost care, compassion, and confidentiality.</li>
                <li><b>Personalized Readings:</b> No two lives are the same, and neither are our readings. Whether you’re looking for insights on love, relationships, career, or life’s biggest questions, we tailor our approach to meet your unique needs.</li>
                <li><b>24/7 Availability:</b> Life’s questions don’t always wait for the perfect time. That’s why Ohio Psychics is available around the clock. Call us anytime, day or night, and connect with a trusted psychic advisor who is ready to listen and provide guidance.</li>
            </ul>

            <h3>How It Works</h3>

            <ol>
                <li><b>Choose Your Psychic:</b> Browse our list of talented psychics to find the advisor that resonates with you. Read their profiles and reviews to find the perfect match.</li>
                <li><b>Make the Call:</b> Dial our 1-800 number and be instantly connected to your chosen psychic. Our service is fast, easy, and designed to give you the answers you need when you need them.</li>
                <li><b>Receive Your Reading:</b> Sit back, relax, and let our psychic guide you through the insights and answers you’re seeking. Whether it’s a quick question or an in-depth session, our advisors are here to help.</li>

            </ol>

            <h3>Connect with Ohio Psychics Today</h3>

            <p>
                Don’t let uncertainty hold you back. Discover the clarity and peace of mind that come with a reading from Ohio Psychics. Our trusted advisors are just a phone call away, ready to help you uncover the answers that lie within.

            </p>
            <p>
                Call us now at 1-800-OHIO-PSY and start your journey to enlightenment today!
            </p>

            <h3>News</h3>
            <p>
                Our annual conference has been cancelled due to unforseen circumstances.
            </p>
        </div>
    )

}

export const Home = () => {
    const { state } = useStateDispatch();
    return state.token
        ? (<AuthenticatedHome />)
        : (<UnauthenticatedHome />)
};