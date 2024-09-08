<script lang="ts">
    export let buttonText: string;
    export let buttonColor: "primary" | "secondary" | "accent" | "special";
    export let buttonLink = "#";
    ("primary");

    export let special = "";
    if (buttonColor === "special") {
        special = "bg-gradient-to-r from-primary to-accent";
    }
</script>

<button
    class="btn btn-{buttonColor} text-2xl {special} rounded-lg w-64 transition-all hover:scale-105 hover:text-white"
    on:click={() => (window.location.href = buttonLink)}>{buttonText}</button
>
