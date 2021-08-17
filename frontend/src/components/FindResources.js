import React, { useState } from "react";

import { Col, Input, InputGroup, InputGroupAddon, Row,
        Card, CardImg, CardBody, CardSubtitle, CardHeader, CardText, Button } from "reactstrap";

function FindResources() {
  const [query,updateQuery] = useState();
  const [searchResults, setSearchResults] = useState([]);
  const callAPI = query => {
    fetch(`http://localhost:5000/?q=${query}`)
        .then(res => res.json())
            .then(data => {
                setSearchResults(data)
            })
        .catch(err => console.log(err))
    }


  return (
    <div className="container-fluid">
        <h1>Need Help Finding Resources?</h1>
      <Row>
        <Col>
          <div className="search">
            <InputGroup>
              <InputGroupAddon addonType="append"> Search </InputGroupAddon>
              <Input
                onChange={e => updateQuery(e.target.value.toLocaleLowerCase())}
                value={query}
              />
              <Button onClick={()=>callAPI(query)}>Test</Button>
            </InputGroup>
          </div>
        </Col>
      </Row>
      <div className="results">
            <h2>Youtube Results</h2>
             <Row>
                <Col>
            {searchResults.map(result => (
                
                    <Card className="result-card" key={result.idx}>
                        <CardHeader>{result.title}</CardHeader>
                        <CardBody>
                        <CardImg top width="100%" src="/yt-logo.png" alt="Card image cap" />
                        {/* <CardTitle tag="h5">{result.title}</CardTitle> */}
                        <CardSubtitle tag="h6" className="mb-2 text-muted">{result.views}</CardSubtitle>
                        <CardText><a className="btn" href= {result.links}>Check it Out!</a> {result.views}</CardText>
                        </CardBody>
                    </Card>
                ))}
                </Col>
            </Row>
        </div>
    </div>
  );
}

export default FindResources;