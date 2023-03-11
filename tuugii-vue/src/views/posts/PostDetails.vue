<template>
    <div>
        <h1>{{ $router.params.id }}</h1>
        <Fullpost postid=$router.params.id />
    </div>
</template>

<script>
import Fullpost from '@/components/Fullpost.vue';
export default {
    name: 'postDetails-main',
    components:{
        Fullpost
    },
    data(){
        return{
            postID: this.$router.params.id
        }
    }
}
</script>

<style>

</style>