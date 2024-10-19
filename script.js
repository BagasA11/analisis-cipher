// Frekuensi huruf rata-rata dalam bahasa Inggris (dalam persen)
const englishFrequencies = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09, 
    'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 
    'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 
    'y': 1.97, 'z': 0.07
};

// Inisialisasi chart
let frequencyChart;

function analyzeFrequency() {
    const inputText = document.getElementById('inputText').value.toLowerCase();
    const letterCount = {};
    let totalLetters = 0;

    // Hitung jumlah kemunculan huruf dalam teks yang diinputkan
    for (let i = 0; i < inputText.length; i++) {
        const char = inputText[i];
        if (char >= 'a' && char <= 'z') {
            letterCount[char] = (letterCount[char] || 0) + 1;
            totalLetters++;
        }
    }

    // Siapkan data untuk chart
    const labels = [];
    const frequencies = [];
    const englishFrequenciesData = [];

    for (let letter in englishFrequencies) {
        labels.push(letter.toUpperCase());
        frequencies.push(((letterCount[letter] || 0) / totalLetters * 100).toFixed(2));
        englishFrequenciesData.push(englishFrequencies[letter].toFixed(2));
    }

    // Hapus chart sebelumnya jika ada
    if (frequencyChart) {
        frequencyChart.destroy();
    }

    // Buat chart baru
    const ctx = document.getElementById('frequencyChart').getContext('2d');
    frequencyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Frekuensi Teks (%)',
                    data: frequencies,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Frekuensi Bahasa Inggris (%)',
                    data: englishFrequenciesData,
                    backgroundColor: 'rgba(153, 102, 255, 0.6)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Frekuensi (%)'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Perbandingan Frekuensi Huruf'
                }
            }
        }
    });
}