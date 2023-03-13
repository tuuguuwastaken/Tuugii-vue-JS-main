<template>
    <div>
        <Button text="delete post" color="red" path="/"  @click="getAgreement($route.params.id)"/>
        <h1>{{ $route.params.id }}</h1>
        <Fullpost :postid="$route.params.id" />
        <Button path="/" color="green" text="Go back home"/>

    </div>
</template>

<script>
import Fullpost from '@/components/Fullpost.vue';
import Button from '@/components/Button.vue'
import axios from 'axios'

export default {
    name: 'postDetails-main',
    components:{
        Fullpost,
        Button
    },
    data(){
        return{
            
        }
    },
    methods:{
        getAgreement(id){
            // console.log('https://jsonplaceholder.typicode.com/posts/'+id)
            if (confirm("Press a button!")) {
                axios.delete('https://jsonplaceholder.typicode.com/posts/'+id)
                    .then(result =>{
                        console.log(result.data)
                    })
                    .catch(err => {
                        console.log(err)
                    })
                } else {
                console.log("yeets")
            }
        }
    }
}
</script>

<style>

</style>