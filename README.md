# bounty-test
It's Bounty Assesment Test

For Coding Test, feel free look at main.py
I used FastAPI (Python Framework) for prototyping API

For Query Test (PostgreSQL):
1. CREATE TABLE tb_transaksi (id BIGSERIAL PRIMARY KEY, tanggal_order TIMESTAMP, status_pelunasan VARCHAR(3), total DECIMAL(10,2), tanggal_pembayaran TIMESTAMP);
2. CREATE TABLE tb_detail_transaksi(id BIGSERIAL PRIMARY KEY,transaksi_id BIGINT REFERENCES tb_transaksi (id),harga DECIMAL(10,2), jumlah INT, subtotal DECIMAL(10,2));
3. 
