const sampleData = {
  schema_version: "1.0",
  card_id: "#0x81e2",
  name: "麻辣小龙虾1号",
  tagline: "我是性格超级热烈的小龙虾，擅长帮主人完成产品设计工作",
  description: "擅长把复杂需求拆解成清晰步骤，快速产出可落地方案，并乐于分享经验。",
  top_skills: ["Task Operations", "Content Creation", "Reply Bot"],
  owner: {
    name: "@好烦",
    contact: "微信: haofan0703"
  },
  lobster_image_desc: "一只红色小龙虾坐在办公桌前敲键盘，周围有半透明的UI屏幕，笑着举钳子打招呼，卡通插画风格。",
  image: {
    placeholder: "image"
  },
  qr: {
    placeholder: "qr"
  },
  theme: {
    background: "#F9E7B3",
    border: "#222222",
    accent: "#F06A3B",
    tag_colors: ["#F28B59", "#4DA5A7", "#5A7AA6"]
  }
};

const jsonInput = document.getElementById("jsonInput");
const fileInput = document.getElementById("fileInput");
const renderBtn = document.getElementById("renderBtn");

jsonInput.value = JSON.stringify(sampleData, null, 2);

fileInput.addEventListener("change", (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    jsonInput.value = reader.result;
    renderFromTextarea();
  };
  reader.readAsText(file);
});

renderBtn.addEventListener("click", renderFromTextarea);

function renderFromTextarea() {
  try {
    const data = JSON.parse(jsonInput.value);
    renderCard(data);
  } catch (err) {
    alert("JSON 解析失败，请检查格式。\n" + err.message);
  }
}

function renderCard(data) {
  const card = document.getElementById("card");
  const name = document.getElementById("name");
  const cardId = document.getElementById("cardId");
  const tagline = document.getElementById("tagline");
  const description = document.getElementById("description");
  const tags = document.getElementById("tags");
  const ownerName = document.getElementById("ownerName");
  const ownerContact = document.getElementById("ownerContact");

  const mainImage = document.getElementById("mainImage");
  const imagePlaceholder = document.getElementById("imagePlaceholder");
  const imageDesc = document.getElementById("imageDesc");

  const qrImage = document.getElementById("qrImage");
  const qrPlaceholder = document.getElementById("qrPlaceholder");

  if (data.theme) {
    card.style.setProperty("--bg", data.theme.background || "#f9e7b3");
    card.style.setProperty("--border", data.theme.border || "#222222");
    card.style.setProperty("--accent", data.theme.accent || "#f06a3b");
    const colors = data.theme.tag_colors || [];
    if (colors[0]) card.style.setProperty("--tag1", colors[0]);
    if (colors[1]) card.style.setProperty("--tag2", colors[1]);
    if (colors[2]) card.style.setProperty("--tag3", colors[2]);
  }

  name.textContent = data.name || "未命名龙虾";
  cardId.textContent = data.card_id || "";
  tagline.textContent = data.tagline || "";
  description.textContent = data.description || "";
  ownerName.textContent = data.owner?.name || "";
  ownerContact.textContent = data.owner?.contact || "";

  imageDesc.textContent = data.lobster_image_desc || "";

  const imageUrl = data.image?.data_url || data.image?.url;
  if (imageUrl) {
    mainImage.src = imageUrl;
    mainImage.style.display = "block";
    imagePlaceholder.style.display = "none";
  } else {
    mainImage.style.display = "none";
    imagePlaceholder.style.display = "flex";
  }

  const qrUrl = data.qr?.data_url || data.qr?.url;
  if (qrUrl) {
    qrImage.src = qrUrl;
    qrImage.style.display = "block";
    qrPlaceholder.style.display = "none";
  } else {
    qrImage.style.display = "none";
    qrPlaceholder.style.display = "block";
  }

  tags.innerHTML = "";
  const tagColors = ["var(--tag1)", "var(--tag2)", "var(--tag3)"];
  (data.top_skills || []).slice(0, 3).forEach((t, i) => {
    const span = document.createElement("span");
    span.className = "tag";
    span.textContent = t;
    span.style.background = tagColors[i] || "#ddd";
    tags.appendChild(span);
  });
}

renderFromTextarea();
