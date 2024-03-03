const express = require('express');
const path = require('path'); // Require path module separately
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const router = require('./routes/signup.js');
const cors = require('cors');


const app = express();
const PORT = process.env.PORT || 3000;



app.use(cors());
app.use(bodyParser.json({ extended: true }));
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/', router);



mongoose.connect('mongodb+srv://ishpreet956:PPOatMS24@cluster0.nrhttna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',{
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(()=>{
    app.listen(PORT,()=>{
        console.log(`Server is running on port ${PORT}`);
    })
}).catch((err)=>{
    console.log(err);
});

