<script lang="ts">
    import Button from "./Button.svelte";

    export let buttonText: string;
    export let buttonColor = "accent";
    export let buttonLink = "#";
    export let imageUrl = "path/to/your/image.jpg";
    export let subText = "This is a hero section";
    export let motivator = "For this reason, act!";
</script>

<div class="flex items-center justify-between min-h-[80vh]">
    <div class="flex-1 mr-8">
        <h1 class="text-7xl text-white font-bold">
            When every <span
                class="bg-gradient-to-r from-primary via-blue-200 to-accent bg-clip-text text-transparent"
                >watt</span
            > counts
        </h1>
        <p class="text-2xl mt-8 mb-10">{subText}</p>
        <div class="flex flex-row items-center gap-10 mt-20">
            <Button {buttonText} {buttonColor} {buttonLink}></Button>
            <p class="text-2xl font-bold">{motivator}</p>
        </div>
    </div>
    <img
        class="w-72 h-auto rounded-lg drop-shadow-xl transform hover:scale-105 hover:rotate-3 hover:bg-slate-100 hover:opacity-80 transition-all"
        src={imageUrl}
        alt="Hero Image"
    />
</div>
