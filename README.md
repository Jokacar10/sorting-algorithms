# 🔄 Sorting Algorithms

**Comprehensive collection of sorting algorithms with specialized implementations for blockchain, trading, and data analysis.**

[![GitHub stars](https://img.shields.io/github/stars/Jokacar10/sorting-algorithms?style=social)](https://github.com/Jokacar10/sorting-algorithms/stargazers)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![TypeScript](https://img.shields.io/badge/TypeScript-Ready-blue)](https://www.typescriptlang.org/)

## 🎯 Overview

Production-ready sorting algorithms optimized for:
- 💰 **Blockchain & Crypto** - Transaction, UTXO, token sorting
- 📊 **Trading & Finance** - Price, volume, liquidity ranking
- 🔗 **Data Indexing** - Large-scale blockchain data ordering
- 🧠 **AI & Agents** - Risk severity, relevance ranking

## ✨ Features

✅ **Multiple Implementations**
- Python (NumPy optimized)
- TypeScript/JavaScript
- Go (concurrent sorting)
- Rust (high-performance)

✅ **Specialized Algorithms**
- Classic sorts (Bubble, Quick, Merge, Heap)
- Counting & Radix sorts (non-comparable data)
- Adaptive sorts (partially sorted data)
- Crypto-optimized sorts

✅ **Production Ready**
- Comprehensive test suite
- Performance benchmarks
- Memory profiling
- Edge case handling

✅ **Real-world Use Cases**
- UTXO coin selection
- DEX liquidity ranking
- Exchange pair sorting
- Blockchain data indexing

## 🚀 Quick Start

### Installation

**Python:**
```bash
pip install sorting-algorithms
```

**Node.js:**
```bash
npm install @jokacar10/sorting-algorithms
```

**Go:**
```bash
go get github.com/Jokacar10/sorting-algorithms
```

### Basic Usage

**Python Example:**
```python
from sorting_algorithms import QuickSort, CryptoSort

# Regular sorting
data = [64, 25, 12, 22, 11]
sorter = QuickSort()
sorted_data = sorter.sort(data)

# Crypto-optimized: Sort UTXOs by value
utxos = [
    {'txid': 'abc...', 'value': 1000},
    {'txid': 'def...', 'value': 5000},
    {'txid': 'ghi...', 'value': 200},
]
crypto_sort = CryptoSort()
sorted_utxos = crypto_sort.sort_utxos(utxos, key='value')
```

**JavaScript Example:**
```javascript
const { QuickSort, TradingSort } = require('@jokacar10/sorting-algorithms');

// Sort trading pairs by volume
const pairs = [
    { symbol: 'BTCUSDT', volume: 500000 },
    { symbol: 'ETHUSDT', volume: 300000 },
];

const sorter = new TradingSort();
const sorted = sorter.sortByVolume(pairs, 'desc');
```

## 📚 Documentation

### Core Algorithms
- [Quick Sort](./docs/algorithms/quick-sort.md)
- [Merge Sort](./docs/algorithms/merge-sort.md)
- [Heap Sort](./docs/algorithms/heap-sort.md)
- [Radix Sort](./docs/algorithms/radix-sort.md)

### Specialized Implementations
- [Crypto Sorting](./docs/crypto-sorting.md) - UTXO, NFT, tokens
- [Trading Sorting](./docs/trading-sorting.md) - Pairs, candles, orders
- [Blockchain Indexing](./docs/blockchain-indexing.md) - Transactions, blocks

### Integration Guides
- [Binance Connector Integration](./docs/integration/binance.md)
- [TON API Integration](./docs/integration/ton.md)
- [Wallet SDK Integration](./docs/integration/wallet.md)
- [DEX Integration](./docs/integration/dex.md)

### Performance
- [Benchmarks](./docs/BENCHMARKS.md)
- [Performance Tuning](./docs/PERFORMANCE.md)
- [Memory Analysis](./docs/MEMORY.md)

## 🔗 Real-World Applications

### Trading & Exchanges
```python
# Sort trading pairs by 24h volume
from sorting_algorithms import TradingSort

pairs = binance_client.get_all_tickers()
sorter = TradingSort()
top_100 = sorter.sort_by_volume(pairs, limit=100)
```

### Wallets & UTXOs
```python
# Coin selection algorithm
from sorting_algorithms import CryptoSort

utxos = wallet.get_unspent_outputs()
sorter = CryptoSort()
selected = sorter.select_coins(utxos, target_amount)
```

### DEX & Liquidity
```python
# Sort pools by APY
from sorting_algorithms import DeFiSort

pools = dex_api.get_all_pools()
sorter = DeFiSort()
best_pools = sorter.sort_by_apy(pools, limit=50)
```

### Blockchain Indexing
```python
# Index transactions by timestamp
from sorting_algorithms import BlockchainSort

transactions = node.get_mempool()
sorter = BlockchainSort()
indexed = sorter.index_by_timestamp(transactions)
```

## 📊 Algorithm Comparison

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable | Best For |
|-----------|-----------|------------|-------|--------|----------|
| **Quick Sort** | O(n log n) | O(n²) | O(log n) | ❌ | General purpose, large datasets |
| **Merge Sort** | O(n log n) | O(n log n) | O(n) | ✅ | Stable sorting, linked lists |
| **Heap Sort** | O(n log n) | O(n log n) | O(1) | ❌ | Memory constrained |
| **Counting Sort** | O(n+k) | O(n+k) | O(k) | ✅ | Integers, ranking |
| **Radix Sort** | O(nk) | O(nk) | O(n+k) | ✅ | Strings, large integers |

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test suite
pytest tests/test_trading_sort.py -v

# With coverage
pytest tests/ --cov=sorting_algorithms
```

## 📈 Benchmarks

```bash
# Run benchmarks
python benchmarks/run_all.py

# Compare implementations
python benchmarks/compare.py --algorithms quick,merge,heap --size 1000000
```

Results:
```
Quick Sort (1M items):  0.08s
Merge Sort (1M items): 0.12s
Heap Sort (1M items):  0.10s
Radix Sort (1M items): 0.05s
```

## 🔗 Integration Examples

### ✅ Binance Connector
```bash
pip install sorting-algorithms binance-connector
python examples/binance_top_pairs.py
```

### ✅ GO Wallet SDK
```bash
go get github.com/Jokacar10/go-wallet-sdk
go run examples/wallet_coin_selection.go
```

### ✅ TON API
```bash
pip install sorting-algorithms pytonlib
python examples/ton_transaction_indexing.py
```

### ✅ UniSat Wallet
```bash
npm install @jokacar10/sorting-algorithms
npm run examples:unisat-tokens
```

### ✅ DEX (STON.fi)
```bash
npm install omniston-sdk sorting-algorithms
npm run examples:dex-liquidity
```

## 🛣️ Roadmap

- [x] Core sorting algorithms
- [x] Crypto-optimized implementations
- [x] Trading-specific sorts
- [ ] Concurrent sorting (multi-threaded)
- [ ] GPU-accelerated sorting
- [ ] Real-time streaming sort
- [ ] Custom comparator builders
- [ ] Caching layer for repeated sorts

## 🤝 Contributing

Contributions welcome! Areas to help:
- New algorithm implementations
- Performance optimizations
- New integrations
- Documentation
- Bug fixes

See [CONTRIBUTING.md](CONTRIBUTING.md)

```bash
git clone https://github.com/Jokacar10/sorting-algorithms.git
cd sorting-algorithms
pip install -e ".[dev]"
pytest
```

## 📦 Directory Structure

```
sorting-algorithms/
├── src/
│   ├── core/                    # Basic algorithms
│   │   ├── quick_sort.py
│   │   ├── merge_sort.py
│   │   └── heap_sort.py
│   ├── crypto/                  # Blockchain-specific
│   │   ├── utxo_sort.py
│   │   ├── nft_sort.py
│   │   └── token_sort.py
│   ├── trading/                 # Trading/Exchange
│   │   ├── pair_sort.py
│   │   ├── candle_sort.py
│   │   └── order_sort.py
│   ├── defi/                    # DeFi operations
│   │   ├── liquidity_sort.py
│   │   ├── pool_sort.py
│   │   └── yield_sort.py
│   └── indexing/                # Blockchain indexing
│       ├── transaction_sort.py
│       ├── block_sort.py
│       └── address_sort.py
├── tests/
│   ├── test_core/
│   ├── test_crypto/
│   ├── test_trading/
│   ├── test_defi/
│   └── test_indexing/
├── benchmarks/
│   ├── core_benchmarks.py
│   ├── crypto_benchmarks.py
│   └── compare.py
├── examples/
│   ├── binance_top_pairs.py
│   ├── wallet_coin_selection.py
│   ├── ton_transactions.py
│   ├── unisat_tokens.py
│   └── dex_liquidity.py
├── docs/
│   ├── algorithms/
│   ├── crypto-sorting.md
│   ├── trading-sorting.md
│   ├── blockchain-indexing.md
│   ├── integration/
│   ├── BENCHMARKS.md
│   └── PERFORMANCE.md
├── pyproject.toml
├── tsconfig.json
├── go.mod
└── README.md
```

## 📞 Support 

- 📚 [Full Documentation](./docs/)
- 💬 [Discussions](https://github.com/Jokacar10/sorting-algorithms/discussions)
- 🐛 [Issues](https://github.com/Jokacar10/sorting-algorithms/issues)
- 🌐 [Website](https://sorting-algorithms.dev)

## 📄 License

Apache License 2.0 - © 2024 Jokacar10

---

**Production-ready sorting for blockchain, trading, and data analysis. [Get Started →](./docs/GETTING_STARTED.md)**
