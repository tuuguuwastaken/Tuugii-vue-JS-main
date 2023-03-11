<template>
  <div>
    <h3>{{ post.title }}</h3>
    <P>{{ post.body }}</P>
    <hr>
    <div v-for="comment in comments" :key="comment.id">
        <P>{{ comment.body }}</P>
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
            post:[],
            comments:[]
        }
    },
    mounted(){
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

<style>
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
    }
    p{
        font-size: 14px;
    }
    .body-text{
        font-size: 20px;
        font-weight: lighter;
    }

</style>