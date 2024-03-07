const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name:{
    type: String,
    // required:true
  },
  phone:{
    type:Number,
    // required:true
},
 password:{
  type:Number,
  required:true
 },
 username:{
      type:String,
      // required:true 
  },
  email:{
    type:String,
    required:true
  },
 
  qual:{
    type:String,
    // required:true
  }

});

const User = mongoose.model('User', userSchema);

module.exports = User;
