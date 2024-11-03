document.addEventListener('DOMContentLoaded', function() {
    const stripe = Stripe(document.getElementById('id_stripe_public_key').textContent);
    const elements = stripe.elements();

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

    cardElement.on('change', function(event) {
        const displayError = document.getElementById('card-errors');
        displayError.textContent = event.error ? event.error.message : '';
    });

    document.getElementById('payment-form').addEventListener('submit', async function(event) {
        event.preventDefault();

        const { error, paymentIntent } = await stripe.confirmCardPayment(document.getElementById('id_client_secret').textContent, {
            payment_method: {
                card: cardElement,
                billing_details: {
                    name: document.querySelector('input[name="full_name"]').value,
                    email: document.querySelector('input[name="email"]').value,
                    // Include other fields as necessary
                }
            }
        });

        if (error) {
            document.getElementById('card-errors').textContent = error.message;
        } else if (paymentIntent.status === 'succeeded') {
            // Payment was successful, now submit the form to complete the order
            const form = document.getElementById('payment-form');
            form.submit();
        }
    });
});
