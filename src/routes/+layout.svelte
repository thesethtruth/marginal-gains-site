<script lang="ts">
    import Footer from "$lib/Footer.svelte";
    import Header from "$lib/Header.svelte";
    import "../app.css";
</script>

<div class="">
    <Header />
    <div class="container mx-auto max-w-6xl mb-auto px-10 mt-20">
        <slot />
    </div>
    <Footer />
</div>
