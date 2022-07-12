# bounty-test
It's Bounty Assesment Test
https://docs.google.com/document/d/10bexswLi2zzZrjrBGHhfnhLWGVQkj1fsxsVcSqLlTms/edit

For Coding Test, feel free look at main.py
I used FastAPI (Python Framework) for prototyping API

For Query Test (PostgreSQL):
1. CREATE TABLE tb_transaksi (id BIGSERIAL PRIMARY KEY, tanggal_order TIMESTAMP, status_pelunasan VARCHAR(3), tanggal_pembayaran TIMESTAMP);
2. CREATE TABLE tb_detail_transaksi(id BIGSERIAL PRIMARY KEY,transaksi_id BIGINT REFERENCES tb_transaksi (id),harga DECIMAL(10,2), jumlah INT, subtotal DECIMAL(10,2));
3. 
