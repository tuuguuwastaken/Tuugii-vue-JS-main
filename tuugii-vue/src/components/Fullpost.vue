<template>
  <div class="container">
    <div class="postFull">
        <h3 class="post-title">{{ posts.title }}</h3>
        <h4 class="post-body">{{ posts.body }}</h4>
    </div>
    <hr/>
    <div v-for="comment in comments" :key="comment.id">
        <div class=" comments">      
            <p><strong>{{ comment.name }} </strong></p>
            <p><strong>{{ comment.email }}</strong></p>
            <P>{{ comment.body }}</P>
        </div>    
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name:'Postfull-main',
    props:{
        postid: {
            required: true,
        }
    },
    data(){
        return{
            posts:[],
            comments:[]
        }
    },
    mounted(){
        // console.log(this.$route)
        axios.get(`https://jsonplaceholder.typicode.com/posts/`+this.postid)
            .then(results =>{
                this.posts = results.data;
            })
            .catch(err =>{
                console.log(err);
            });
        axios.get(`https://jsonplaceholder.typicode.com/comments?postId=`+this.postid)
            .then(results =>{
                this.comments = results.data;
            })
            .catch(err =>{
                console.log(err)
            })
    }
}
</script>

<style scoped>

    .comments{
        overflow: auto;
        border: 1px solid steelblue;
        padding: 10px;
        border-radius: 5px;
        margin-top: 15px
    }
    .post-body{
        margin-left: 1rem;
        margin-top:13px;
    }
    .postFull{
        margin-left: 1rem;
        margin-bottom: 2rem; 
    }
    .comments{
        margin: 0px,5px,12px,5px;
    }
    .btn-comments{
        margin-top:10px;
    }
    .btn{
        background-color:rgb(10, 110, 192);
    }
    p{
        margin-top:0.5rem;
    }
    .post-title{
        display: flex;
        justify-content: space-between;
        align-items:flex-start;
    }
    .container{
        
        font-size: 20px;
        text-align: left;
        border: 1px solid rgb(130, 196, 235);
        margin-bottom: 4px;
        padding: 9px;
        border-radius: 12px;
    }
    h4{
    font-size: 18px;
    font-weight: lighter;
    }
    p{
        font-size: 14px;
    }
    .body-text{
        font-size: 20px;
        font-weight: lighter;
    }

</style>