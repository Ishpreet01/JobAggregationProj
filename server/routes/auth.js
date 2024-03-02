const express=require('express');
const authController = require('../controllers/authController.js');

const router=express.Router();


router.post('/login',authController.login);
router.get('/get',authController.renderProfilePage);
router.post('/profile',authController.saveUserProfile); 

module.exports = router;
