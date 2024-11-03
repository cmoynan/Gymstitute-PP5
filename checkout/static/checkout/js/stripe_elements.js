document.addEventListener('DOMContentLoaded', function() {
    console.log("Initializing Stripe"); // Check if this log appears
    const stripe = Stripe("{{ stripe_public_key }}");
    const elements = stripe.elements();
    console.log("Stripe initialized"); // Check if this log appears

    const cardElement = elements.create('card', {
        style: {
            base: {
                color: '#32325d',
                fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                fontSize: '16px',
                lineHeight: '24px',
                '::placeholder': {
                    color: '#aab7c4'
                }
            },
            invalid: {
                color: '#fa755a',
                iconColor: '#fa755a'
            }
        }
    });

    cardElement.mount('#card-element');
    console.log("Card element mounted"); // Check if this log appears

    cardElement.on('change', function(event) {
        const displayError = document.getElementById('card-errors');
        displayError.textContent = event.error ? event.error.message : '';
    });

    document.getElementById('payment-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        const form = document.getElementById('payment-form');
        
        const { error, paymentIntent } = await stripe.confirmCardPayment("{{ client_secret }}", {
            payment_method: {
                card: cardElement,
                billing_details: {
                    // Gather form details here
                }
            }
        });

        if (error) {
            document.getElementById('card-errors').textContent = error.message;
        } else if (paymentIntent.status === 'succeeded') {
            form.submit(); // Submit the form to your backend for further processing
        }
    });
});