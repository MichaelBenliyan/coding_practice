import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, Radio, RadioGroup, FormControlLabel} from "@material-ui/core";

export default class CreateRoomPage extends Component {
    defaultVotes = 2;

    constructor(props) {
        super(props);
        this.state = {
            guestCanPause: true, 
            votesToSkip: this.defaultVotes,
        };
        // binds the method to the class. this allows access to the 'this' keyword
        this.handleRoomButtonPressed = this.handleRoomButtonPressed.bind(this);
        this.handleVotesChange = this.handleVotesChange.bind(this);
        this.handleGuestCanPauseChange = this.handleGuestCanPauseChange.bind(this);
    }
    // e is the object that called the function
    handleVotesChange(e) {
        this.setState({
            votesToSkip: e.target.value,
        })
    }
    handleGuestCanPauseChange(e) {
        this.setState({
            guestCanPause: e.target.value === 'true' ? true : false,
        })
    }
    handleRoomButtonPressed() {
        const requestOptions = {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            // can pass a javascript object to be converted into a JSON string
            body: JSON.stringify({
                // following field names need to match what we're looking for in the server
                votes_to_skip: this.state.votesToSkip,
                guest_can_pause: this.state.guestCanPause
            }),
        };
        // i wanna send a request to local host api/create-room || going to send it with the request option || 
        // the .then is saying once we get a response lets take that response and convert that response into JSON 
        // || then lets take the data and do something with the data
        fetch('/api/create-room', requestOptions)
        .then((response) => response.json())
        .then((data) => this.props.history.push('/room/' + data.code));
    }

    render() {
        // spacing is 1 = 8px
        return(
            <Grid container spacing={1} align="center">
                {/* xs, can also have s m l etc, tells us what the width should be when the size of the window is xs, etc... 12 is the maximum value you can put for the value. */}
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create A Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <FormHelperText>
                            <div align="center">
                                Guest Control Of Playback
                            </div>
                        </FormHelperText>
                        <RadioGroup row defaultValue='true' onChange={this.handleGuestCanPauseChange}>
                            <FormControlLabel 
                                value ='true' 
                                control={<Radio color='primary'/>}
                                label="Play/Pause"
                                lavelPlacement="bottom" 
                            />
                            <FormControlLabel 
                                value ='false' 
                                control={<Radio color='secondary'/>}
                                label="No Control"
                                lavelPlacement="bottom" 
                            />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <TextField
                            required={true} 
                            type="number" 
                            onChange={this.handleVotesChange}
                            defaultValue={this.defaultVotes}
                            inputProps={{
                                min: 1,
                                style: { textAlign: 'center' } 
                            }}
                        />
                        <FormHelperText>
                            <div align="center">
                                Votes Required To Skip Song
                            </div>
                        </FormHelperText>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button color="primary" variant="contained" onClick={this.handleRoomButtonPressed} >
                        Create A Room
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button color="secondary" variant="contained" to="/" component={Link}>
                        Back
                    </Button>
                </Grid>
            </Grid>
        );
    }
}