<template> 
  <div>
    
    <q-banner dense class="bg-primary text-white">
        Tennis players Classifier
    </q-banner>
  
    <div   class="column items-center" >   
    
      <div class="row">
        <div class="col">
          <q-uploader
              :factory="uploadFile" 
              style="max-width: 300px"
              :max-files="1"
              multiple = "false"
              @added ="file_selected"
              @removed="init">
          </q-uploader>
          
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div   v-if="recognized === false ">
                The player couldn't be recognized due to image quality, or face position
          </div>
              
          <div class="q-pa-md q-gutter-sm">  
            <q-list class="shadow-2 rounded-borders" style="max-width: 500px; width: 100%;">
                  <q-item v-bind:style="this.playerName === 'maria_sharapova' ?styleObject :'' ">
              
              <q-item-section avatar >
                  <q-avatar style="height: 100px; width: 100px;">
                  <img src="../assets/img/maria.jpeg">
                  </q-avatar>
                </q-item-section>
                <q-item-section>MARIA SHARAPOVA {{this.player1_prob}}</q-item-section>     
              </q-item>

              <q-item v-bind:style="this.playerName === 'ons_jabeur' ?styleObject :'' " >
                <q-item-section avatar>
                  <q-avatar style="height: 100px; width: 100px;">
                  <img src="../assets/img/ons.jpg">
                  </q-avatar>
                </q-item-section>
                <q-item-section>ONS JABEUR {{this.player2_prob}}</q-item-section> 
              </q-item>
              
              <q-item v-bind:style="this.playerName === 'rafael_nadal' ?styleObject :'' " >
                <q-item-section avatar>
                  <q-avatar style="height: 100px; width: 100px;">
                  <img src="../assets/img/nadal.jpg">
                  </q-avatar>
                </q-item-section>
                <q-item-section>RAFAEL NADAL {{this.player3_prob}}</q-item-section>
              </q-item>
            

              <q-item v-bind:style="this.playerName === 'roger_federer' ?styleObject :'' " >
                <q-item-section avatar>
                  <q-avatar style="height: 100px; width: 100px;">
                  <img src="../assets/img/roger.jpeg">
                  </q-avatar>
                </q-item-section>
                <q-item-section>ROGER FEDERER {{this.player4_prob}}</q-item-section>
              </q-item>

              <q-item v-bind:style="this.playerName === 'serena_williams' ?styleObject :'' " >
                <q-item-section avatar>
                  <q-avatar style="height: 100px; width: 100px;">
                  <img src="../assets/img/serena.jpeg">
                  </q-avatar>
                </q-item-section>
                <q-item-section>SERENA WILLIAMS {{this.player5_prob}} </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>
      </div>
    
    </div> 
    <div   v-if="error ">
      Something went wrong!!
    </div>
  </div>   
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'IndexPage',
  data() {
  return {
    selected_file:'',
    player1_prob:'',
    player2_prob:'',
    player3_prob:'',
    player4_prob:'',
    player5_prob:'',
    playerName:'',
    response:'',
    recognized :true,
    error: false,
    styleObject: { 'background-color' : 'coral'},

  }
},
  methods:{
    file_selected(file) {
  this.selected_file = file[0];
},


init(){
  this.player1_prob = ''
  this.player2_prob = ''
  this.player3_prob = ''
  this.player4_prob = ''
  this.player5_prob = ''
  this.playerName = ''
  this.recognized =true
},


async asyncFunc(formData){
       await axios.post( 'http://127.0.0.1:5000/classify_image',
      formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }
       ).then((response) => {
              this.response = response
          
          
        }, (error) => {
           this.eroor = true
          })
},

uploadFile() {
  let formData = new FormData();
      const reader = new FileReader()
      //convert the image into base64 url
      let rawImg;
      reader.readAsDataURL(this.selected_file);
      reader.onloadend = () => {
      rawImg = reader.result;
      formData.append('image_data',rawImg);
      this.init()
      this.asyncFunc(formData).then(
        res => {

         if (this.response.data[0] !== undefined)
            {
              // get the player match
              this.playerName = this.response.data[0].class
              //get the payers probability
              this.player1_prob = " has a probability of : "+ this.response.data[0].class_probability[0]+ "%"
              this.player2_prob = " has a probability of : "+ this.response.data[0].class_probability[1]+ "%"
              this.player3_prob = " has a probability of : "+ this.response.data[0].class_probability[2]+ "%"
              this.player4_prob = " has a probability of : "+ this.response.data[0].class_probability[3]+ "%"
              this.player5_prob = " has a probability of : "+ this.response.data[0].class_probability[4]+ "%"       

           }
           else{
             this.recognized = false
           }
                    })
      }
},

  }
 
})
</script>
