const User = require('../models/User.js');

const login=(req,res)=>{
    res.redirect('/profile');
};


const renderProfilePage = (req, res) => {
    // Render profile page with form for entering user information
    res.render('CreateProfile');
  };

const saveUserProfile = (req, res) => {
    // Retrieve user information from request body
    const { name, email, phoneNumber } = req.body;
  
    // Create new user instance
    const newUser = new User({
      name,
      email,
      phoneNumber
    });
  
    // Save user to MongoDB
    newUser.save()
      .then(() => {
        res.send('User information saved successfully');
      })
      .catch((error) => {
        console.error(error);
        res.status(500).send('Internal server error');
      });
  };
  
  module.exports = {
    login,
    renderProfilePage,
    saveUserProfile
  };