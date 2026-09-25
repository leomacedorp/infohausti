import { NextResponse } from 'next/server';
import { stripe } from '@/lib/stripe';

export async function POST(req: Request) {
  try {
    const body = await req.json().catch(() => ({}));
    const { priceId, successUrl, cancelUrl, customerEmail } = body;

    const origin = req.headers.get('origin') || 'http://localhost:3000';

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card', 'boleto'],
      line_items: [
        {
          price: priceId || process.env.DEFAULT_STRIPE_PRICE_ID,
          quantity: 1,
        },
      ],
      mode: 'payment',
      customer_email: customerEmail || undefined,
      success_url: successUrl || `${origin}/sucesso?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: cancelUrl || `${origin}/?canceled=true`,
      allow_promotion_codes: true,
      billing_address_collection: 'required',
    });

    return NextResponse.json({ sessionId: session.id, url: session.url });
  } catch (error: any) {
    console.error('Erro ao criar sessão de checkout:', error);
    return NextResponse.json(
      { error: error?.message || 'Erro interno no servidor' },
      { status: 500 }
    );
  }
}
