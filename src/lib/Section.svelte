<script lang="ts">
    import Button from "./Button.svelte";

    export let title;
    export let subtitle;
    export let paragraph;
    export let imageSrc;
    export let color: "primary" | "secondary" | "accent" = "accent";
    export let leadcols = 3;
    export let leadrows = 4;
    export let buttonText = "Click me";
    export let buttonLink = "#";

    const leadelements = leadcols * leadrows;
</script>

<section class="flex col-1 flex-col items-center gap-2 mt-20 min-h-[80vh]">
    <div class="lead-grid bg-clip-text grid-cols-3 gap-0">
        {#each Array(leadelements) as _, i}
            <div class="bg-{color} w-2 h-2 rounded-full m-0 p-0" />
        {/each}
    </div>
    <div
        class="text-bg w-fit m-2 py-2 font-black text-5xl border-b-8 border-{color} text-center pb-4"
    >
        {title}
    </div>
    <h2 class="text-white font-semibold text-2xl text-{color} mb-4">
        {subtitle}
    </h2>
    <!-- start of details -->
    <div class="grid grid-cols-2 w-3/4 gap-5 mt-10">
        <div class="flex items-center w-full">
            <p class="mb-4 text-lg text-right">{paragraph}</p>
        </div>
        <div class="flex items-center justify-center">
            <img
                src={imageSrc}
                alt="Depection of {title}"
                class="w-2/4 rounded-lg transition-all hover:-rotate-3 hover:scale-105"
            />
        </div>
        <div class="flex justify-end">
            <Button buttonColor={color} {buttonText} {buttonLink} />
        </div>
    </div>
</section>

<style>
    .lead-grid {
        background-position: center;
        display: grid;
        gap: 1rem;
        mask-image: linear-gradient(transparent 0%, black 100%);
        -webkit-mask-image: linear-gradient(transparent 0%, black 100%);
    }
</style>
