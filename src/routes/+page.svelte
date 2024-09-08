<script>
    import Section from "$lib/Section.svelte";
    import Hero from "../lib/Hero.svelte";
</script>

<div
    class="hidden bg-secondary bg-primary bg-accent btn-primary btn-secondary btn-accent btn-alert border bottom-4 bottom-0 border-primary border-accent border-secondary fixed h-4 left-0 right-0 top-4 z-50"
></div>

<Hero
    buttonText="Sign up"
    subText="Transform your ride with expert advice on training, nutrition, gear, and bike positioning. At Marginal Gains, we turn cutting-edge research into actionable strategies to help you achieve peak performance. Join our community and start riding smarter today."
    imageUrl="hero.webp"
    motivator="Ride smarter, not harder!"
    buttonColor="special"
/>

<Section
    title="AERO"
    subtitle="Wheelie Fast: Custom Gear for Serious Speed!"
    paragraph="Upgrade to our bespoke wheels and cockpits designed for optimal aerodynamics. Experience the perfect blend of speed and stability, tailored to your unique riding style. Ride faster, save watts, and achieve your personal best with our innovative aero products."
    imageSrc="hero.webp"
    color="accent"
    buttonText="Shop Now"
/>

<Section
    title="Nutrition"
    subtitle="Food for Thought: Eat, Ride, Repeat!"
    paragraph="Achieve peak performance with our expert nutrition strategies. From on-bike fueling to post-ride recovery, we provide personalized plans based on the latest research. Optimize your energy levels and accelerate your recovery to stay ahead of the pack."
    imageSrc="nutrition.webp"
    color="primary"
    buttonText="Learn More"
/>

<Section
    title="Training"
    subtitle="Sweat Smart: Training Tips That Won't Break the Chain!"
    paragraph="Elevate your training with our data-driven approaches. Implement heat stress protocols and block training to maximize your gains. Our scientifically-backed methods ensure you train efficiently and effectively, leading to significant performance improvements on the road."
    imageSrc="training.webp"
    color="secondary"
    buttonText="Get Started"
/>
