const express = require('express');
const path = require('path'); // Require path module separately
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const authRoutes = require('./routes/auth.js');


const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use('/auth', authRoutes);



mongoose.connect('mongodb+srv://ishpreet956:PPOatMS24@cluster0.nrhttna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',{
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(()=>{
    app.listen(PORT,()=>{
        console.log(`Server is running on port ${PORT}`);
    })
})



// app.get('/', (req, res) => {
//     res.sendFile(path.resolve(__dirname, '../client/src/components/Login/LoginPage.jsx'));
// });

// app.get('/profile',(req,res)=>{
//     res.sendFile(path.resolve(__dirname,'../client/src/components/Profile/CreateProfile.jsx'));
// });



// app.listen(PORT, () => {
//     console.log(`Server is listening at port ${PORT}`);
// });
